# Print the kth line of a file using sed

# Get the first k lines of a file, in place using sed -i

# To count if there are an odd number (unmatched) double quotes
awk -F\" 'NF % 2 == 0' 

# To drop a certain field (2nd here) in a text file
awk -F"\t" '{ $2=""; print}'

# Print the entire line of a tab separated file if the 4th field mathes “IN”
awk -F"\t" '$4=="IN" {print $0}'  location.tsv > india.location.tsv


# Pattern search anywhere in string
`awk': awk -F"\t" 'tolower($8) ~ /indian space/ {print $2","$8} ‘ rawassignee.tsv

