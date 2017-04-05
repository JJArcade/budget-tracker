SELECT sql
  FROM (
        SELECT sql sql, type type, tbl_name tbl_name, name name
          FROM sqlite_master
         UNION ALL
        SELECT sql, type, tbl_name, name
          FROM sqlite_temp_master
       )
 WHERE type != 'meta'
   AND sql NOTNULL
   AND name NOT LIKE 'sqlite_%'
   AND sql LIKE '%REFERENCES%'
ORDER BY substr(type, 2, 1), name;
