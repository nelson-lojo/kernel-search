# Exo's scheduling API

## Top-level Python function decorator

1. `@proc` - decorates a Python function which is parsed and compiled as Exo. Replaces
   the function with a `Procedure` object.
2. `@instr` - same as `@proc`, but accepts a hardware instruction as a format string.
3. `@config` - decorates a Python class which is parsed and compiled as an Exo
   configuration object

## Procedure object methods

**Introspection operations**

- `.name()` returns the procedure name.
- `.check_effects()` forces Exo to run effect checking on the procedure.
- `.show_effects()` prints the effects of the procedure.
- `.show_effect(stmt)` prints the effect of the `stmt` in the procedure.
- `.is_instr()` returns `true` if the procedure has a hardware instruction string.
- `.get_instr()` returns the hardware instruction string.
- `.get_ast()` returns a `QAST`, which is an AST representation suitable for
  introspection.

**Execution / interpretation operations**

- `.compile_c(directory, filename)` compiles the procedure into C and stores
  in `filename` in the `directory`.
- `.interpret(**args)` runs Exo interpreter on the procedure.

## Scheduling operations on Procedure objects

**Buffer related operations**

- `.reuse_buffer(buf1, buf2` 
  - Reuses a buffer `buf1` in the use site of `buf2` and removes the allocation of `buf2`
- `.inline_window(win_stmt)`
  - Removes the window statement `win_stmt`, which is an alias to the window, and inlines the windowing in its use site
- `.expand_dim(stmt, alloc_dim, indexing)`
  - Expands the dimension of the allocation statement `stmt` with dimension `alloc_dim` of indexing `indexing`
- `.bind_expr(new_name, expr)`
  - Binds the right hand side expression `expr` to a newly allocated buffer named `new_name`
- `.stage_mem(win_expr, new_name, stmt_start, stmt_end=None)`
  - Stages the buffer `win_expr` to the new window expression `new_name` in statement block (`stmt_start` to `stmt_end`), and adds an initialization loop and a write-back loop
- `.rearrange_dim(alloc, dimensions)`
  - Takes an allocation statement and a list of integers to map the dimension. It rearranges the dimensions of `alloc` in `dimension` order. E.g., if `alloc` were `foo[N,M,K]` and the `dimension` were `[2,0,1]`, it would become `foo[K,N,M]` after this operation.
- `.lift_alloc(alloc, n_lifts=1, keep_dims=False)`
  - Lifts the allocation statement `alloc` out of `n_lifts` number of scopes. If and For statements are the only statements in Exo which introduce a scope. When lifting the allocation out of a for loop, it will expand its dimension to the loop bound if `keep_dims` is True.

**Loop related operations**

- `.split(loop, split_const, iter_vars, tail='guard', perfect=False)`
  - Splits `loop` into an outer and an inner loop. The inner loop bound is `split_const` and the outer and inner loop names are specified by a list of strings `iter_vars`. If `perfect` is True, it will not introduce a tail case. `tail` specifies the tail strategies, where the options are `guard`, `cut`, and `cut_and_guard`.
- `.fuse_loop(loop1, loop2)`
  - Fuses two adjacent loops with a common iteration variable.
- `.partition_loop(loop, num)`
  - Partitions `loop` into two loops, the first running between `0` and `num` and the second between `num+1` and `loop`'s original bound.
- `.reorder(loop1, loop2)`
  - Reorders two nested loops. `loop2` should be nested directly inside `loop1`. `loop1` will be nested inside `loop2` after this operation.
- `.unroll(loop)`
  - Unrolls the loop. The loop needs to have a constant bound.
- `.fission_after(stmt, n_lifts=1)`
  - Fissions the `n_lifts` number of loops around the `stmt`. The fissioned loops around the `stmt` need to be directly nested with each other and the statements before and after the `stmt` should not have any allocation dependencies.
- `.remove_loop(loop)`
  - Replaces the loop with its body if the body is idempotent. The system must be able to prove that the loop runs at least once.

**Config related operations**

- `.bind_config(expr, config, field)`
  - Binds the right hand side `expr` to `config.field`. It will replace the use site of `expr` with `config.field` and introduces a config statement of `config.field = expr`.
- `.configwrite_root(config, field, expr)`
  - Inserts the config statement `config.field = expr` in the beginning of the procedure.
- `.configwrite_after(stmt, config, field, expr)`
  - Inserts the config statement `config.field = expr` after `stmt`.
- `.delete_config(stmt)`
  - Deletes the configuration statement.

**Other scheduling operations**

- `.add_assertion(assertion)`
  - Asserts the truth of the expression `assertion` at the beginning of the procedure.
- `.lift_if(if, n_lifts=1)`
  - Lifts the if statement `if` out of `n_lifts` number of scopes. This is similar to `reorder()`, but for if statements.
- `.eliminate_dead_code(stmt)`
  - Eliminates `if` statement if condition is always True or False. Eliminates `for` statement if condition is always False.
- `.delete_pass()`
  - Deletes a `Pass` statement in the procedure.
- `.reorder_stmts(stmt1, stmt2)`
  - Reorder two adjacent statements `stmt1` and `stmt2`. After this operation, the order will be `stmt2` `stmt1`.
- `.reorder_before(stmt)`
  - Move the statement `stmt` before the previous statement. This is a shorthand for `reorder_stmts()`.
- `.replace(subproc, stmt)`
  - Replace the statement with a call to `subproc`. This operation is one of our contributions and is explained in detail in the paper.
- `.replace_all(subproc)`
  - Eagerly replace every matching statement with a call to `subproc`.
- `.inline(call_site)`
  - Inline the function call.
- `.is_eq(another_proc)`
  - Returns True if `another_proc` is equivalent to the procedure.
- `.call_eqv(eqv_proc, call_site)`
  - Replace the function call statement of `call_site` with a call to an equivalent procedure `eqv_proc`.
- `.repeat(directive, *args)`
  - Continue to run the directive until it fails. The directive and its arguments are given separately, e.g. `proc.repeat(Procedure.inline, "proc_to_inline(_)")`
- `.simplify()`
  - Simplify the code in the procedure body. Tries to reduce expressions to constants and eliminate dead branches and loops. Uses branch conditions to simplify expressions inside the branches.
- `.rename(new_name)`
  - Rename this procedure to `new_name`.
- `.make_instr(instr_string)`
  - Converts this procedure to an instruction procedure with instruction `instr_string`.
- `.partial_eval(*args, **kwargs)`
  - Specializes this procedure to the given argument values.
- `.set_precision(name, type)`
  - Sets the precision type of `name` to `type`.
- `.set_window(name, is_window)`
  - If `is_window` is True, it sets the buffer `name` to window type, instead of a tensor type.
- `.set_memory(name, mem_type)`
  - Sets a buffer `name`'s memory type to `mem_type`.
