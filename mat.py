def matmul(a, b):
  # ensure the number of columns in a, matches the number of rows in b
  assert len(a[0]) == len(b), "num of columns in a does not match num of rows in b"

  result = []

  # loop through each row of a
  for a_row in range(len(a)):
    # store the result for this row
    result_row = []

    # loop through each column of b (using b[0] to define how many columns there are)
    for b_column in range(len(b[0])):
      # store the sum
      sum = 0
      # loop through each row in the current column of b
      for b_row in range(len(b)):
        sum += a[a_row][b_row] * b[b_row][b_column]

      result_row.append(sum)

    result.append(result_row)

  return result
