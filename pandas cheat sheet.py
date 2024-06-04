'''
Pandas Cheat Sheet

DataFrame
A two-dimensional labeled data structure with columns of potentially different types.
	pd.DataFrame(data, index, columns)
	Arguments:
		data: Data can be a list, dictionary, or a DataFrame.
		index: Index labels. Default is range(n).
		columns: Column labels. Default is range(n).
Example: pd.DataFrame(data, index, columns)

____________________ INDEXING ____________________

Loc
Access a group of rows and columns by labels.
	df.loc[row_label, column_label]
	Arguments:
		row_label: Row label. Default is all rows.
		column_label: Column label. Default is all columns.
Example: df.loc["Joe", "age"] returns the age of Joe.

Iloc
Access a group of rows and columns by integer position.
	df.iloc[row_position, column_position]
	Arguments:
		row_position: Row position. Default is all rows.
		column_position: Column position. Default is all columns.
Example: df.iloc[0, 1] returns the element in the first row and second column.

Head / Tail
Return the first/last n rows.
	df.head(n)
	df.tail(n)
	Arguments:
		n: Number of rows to return. Default is 5.
Example: df.head(3) returns the first 3 rows.
Example: df.tail(3) returns the last 3 rows.

Shape
Return a tuple representing the dimensionality of the DataFrame.
	df.shape
Example: df.shape returns the number of rows and columns.

Index
Return the index (row labels) of the DataFrame.
	df.index
Example: df.index returns the row labels.

Columns
Return the column labels of the DataFrame.
	df.columns
Example: df.columns returns the column labels.

Describe
Generate descriptive statistics.
	df.describe()
Example: df.describe() returns the count, mean, standard deviation, minimum, and maximum values.

Idxmax / Idxmin
Return the index of the first occurrence of the maximum/minimum value.
	df["column"].idxmax()
	df["column"].idxmin()
Example: df["age"].idxmax() returns the index of the oldest person.
Example: df["age"].idxmin() returns the index of the youngest person.

____________________ RENAMING ____________________

Rename
Rename columns.
	df.rename(columns={"old_name": "new_name"}, inplace=True)
	Arguments:
		old_name: Current column name.
		new_name: New column name.
		inplace: Whether to modify the DataFrame in place. Default is False.
Example: df.rename(columns={"age": "years"}) renames the column 'age' to 'years'.

____________________ DELETING ____________________

Drop
Drop specified labels from rows or columns.
	df.drop(labels, axis)
	Arguments:
		labels: Index or column labels to drop.
		axis: Whether to drop rows or columns with missing values (0 or "index", 1 or "columns"). Default is 0.
Example: df.drop("Joe") removes row with index 'Joe'.
Example: df.drop(columns="age") removes column named 'age'.

Dropna
Remove missing values.
	df.dropna(axis)
	Arguments:
		axis: Whether to drop rows or columns with missing values (0 or "index", 1 or "columns"). Default is 0.
Example: df.dropna() removes all rows with any NaN values.
Example: df.dropna(axis=1) removes all columns with any NaN values.

Drop duplicates
Remove duplicate rows.
	df.drop_duplicates(subset)
	Arguments:
		subset: Column label or sequence of labels to consider for identifying duplicates.
Example: df.drop_duplicates(subset="name") removes rows with duplicate names.

Fillna
Fill missing values.
	df.fillna(value)
	Arguments:
		value: Scalar, dict, Series, or DataFrame to fill missing values with.
Example: df.fillna(0) replaces all NaN values with 0.
Example: df.fillna(method="ffill") fills NaN values with the previous value.

____________________ ARITHMETIC ____________________

Apply
Apply a function along an axis of the DataFrame.
	df.apply(func, axis)
	Arguments: 
		func: Function to apply to each column or row.
		axis: Whether to drop rows or columns with missing values (0 or "index", 1 or "columns"). Default is 0.
Example: df.apply(sum, axis=0) applies the sum function along columns.
Example: df.apply(sum, axis=1) applies the sum function along rows.

Applymap
Apply a function element-wise in the DataFrame.
	df.applymap(func)
Example: df.applymap(lambda x: x*2) multiplies each element by 2.

____________________ SORTING ____________________

Sort values
Sort by the values along either axis.
	df.sort_values(by, ascending)
	Arguments:
		by: Column name or list of names to sort by.
		ascending: Whether to sort in ascending order (True) or descending order (False), default is True.
Example: df.sort_values(by="age") sorts the DataFrame by age in ascending order.
Example: df.sort_values(by=["age", "height"], ascending=[True, False]) 
	sorts by age in ascending order and height in descending order.

____________________ STATS ____________________

Value counts
Count unique values.
	df["column"].value_counts()
Example: df.age.value_counts() returns the count of each unique age.

'''