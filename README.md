# test_task_ddl
For the "РУТ КОД" company


[Task](https://github.com/DenisPonizovkin/rc-task-back1/blob/main/README.md)

### Result:
```
CREATE TABLE IF NOT EXISTS public.data
(
    "код" text COLLATE pg_catalog."default",
    "проект" text COLLATE pg_catalog."default",
    "2022" double precision,
    "2023" double precision,
    "2024" double precision,
    "2025" double precision
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.data
    OWNER to <name>;
```
