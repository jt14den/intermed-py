## Index 
### Type   Notes
* obj[val] Select single column or sequence of columns from the DataFrame. Special case conveniences: boolean array (filter rows), slice (slice rows), or boolean DataFrame (set values based on some criterion).
* obj.ix[val] - Selects single row or subset of rows from the DataFrame.
* obj.ix[:, val] - Selects single column of subset of columns.
* obj.ix[val1, val2] - Select both rows and columns.
* reindex method - Conform one or more axes to new indexes.
* xs method	Select single row or column as a Series by label.
* icol, irow methods - Select single column or row, respectively, as a Series by integer location.
* get_value, set_value methods - Select single value by row and column label.”

*Excerpt From: Wes McKinney. “Python for Data Analysis.” iBooks.* 