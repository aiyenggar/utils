# sed or stream editor can be used to print lines - either specific lines, or every other line, or every two lines. Or to match patterns (start, end or both) and print lines in between. You can print a certain range of lines, or the lines in the neighbourhood of a certain line (whose matching condition has been met). !p inverts the matching/printing process. $ is the last line. ^ is the start of a line.

# Print the kth line of a file using sed
sed -n '3'p filename
sed -n '3~2'p filename (from the third print every other line)
sed -n '4,8'p filename (print from the 4th to the 8th line)
sed -n '/Hardware/,6p' (matches the term Hardware and prints from that to 6th line)
sed -n '3,/Security/p' (the other way)
sed -n '/Storage/,+2p' (two lines from match)
sed -n '/Storage/,/Design/g' (all lines from the matched line to Storage to the matched line to Design)

# Get the first k lines of a file, in place using sed -i

# To count if there are an odd number (unmatched) double quotes
awk -F\" 'NF % 2 == 0' 

# To drop a certain field (2nd here) in a text file
awk -F"\t" '{ $2=""; print}'

# Print the entire line of a tab separated file if the 4th field matches “IN”
awk -F"\t" '$4=="IN" {print $0}'  location.tsv > india.location.tsv

# Using an or (||) and (&&) not {!} condition
awk -F"\t" '$1=="8288508" || $1=="8331281" {print $0}' patent.tsv

# Sum a column
awk -F"," '{sum+=$6} END{print sum}'

# Alternatively
awk -F"," '{sum+=$6} END{printf "%.f\n",sum}'

# Pattern search anywhere in string
`awk': awk -F"\t" 'tolower($8) ~ /indian space/ {print $2","$8} ‘ rawassignee.tsv

# Print first line and matched lines
awk -F"," 'NR==1 {print $0}; $1==225 {print $0}' latlong_urbanarea_1.csv 

rsync -r ~/personal /Volumes/2013a\ Data/OneDrive --delete

# grep printing context -B for before -A for after -C if you want same number of lines before and after

# Printing the first line as well as matched lines
grep -E 'patent_id|3959017' input.csv 
sed '1p;/pattern/!d' input.csv
awk 'NR==1 || /pattern/' input.csv

SSH Key Generation
ssh-keygen -t rsa -b 4096 -C "aiyenggar@icloud.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
pbcopy < ~/.ssh/id_rsa.pub
paste this on github.com settings
ssh -T git@github.com

Add to .zshrc
export LC_ALL=en_US.UTF-8
export PATH=/Applications/anaconda3/bin:$PATH

Install homebrew
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null

Installing git-crypt on Mac
To get git-crypt, you needed to update xcode from App Store.
Then download gnupg for os x. The version I have is 2.2.5. 
brew install git-crypt
brew install gpg
brew link --overwrite gnupg


Process to move keys from one machine to another
On source machine
gpg --export -a aiyenggar@icloud.com > public.key
gpg --export-secret-key -a aiyenggar@icloud.com > private.key

On destination machine
gpg --delete-secret-key aiyenggar@icloud.com
gpg --delete-key aiyenggar@icloud.com
gpg --import public.key
gpg --import private.key

You'll notice that the trust level is unknown when you perform a gpg --list-keys
To fix this:
gpg --edit-key aiyenggar@icloud.com
> trust
Your Decision? 5
> save

Ashwin’s Summary:
mkdir folder, add files
git init
git crypt init
fill in .gitattributes file

* filter=git-crypt diff=git-crypt
/** filter=git-crypt diff=git-crypt
*.csv filter=git-crypt diff=git-crypt
.git* !filter !diff

git crypt status
for existing repos: git crypt status -f (But previous commits will just stay as usual)
git add *
git commit -m “message"
Create the repository on github.com

git remote add origin git@github.com:aiyenggar/summer.git
git push -u origin master

Checking out an existing project
git clone git@github.com:aiyenggar/utils.git

Troubleshooting
Incase the repository was cloned from the desktop app prior to the ssh setting

git config --global user.name "Ashwin"
git config --global user.email "aiyenggar@users.noreply.github.com"
git remote set-url origin git@github.com:aiyenggar/econometrics.git

git crypt status
git crypt lock
git crypt unlock

The locking unlocking process on git crypt
locking is easy. git crypt lock.
To unlock, you first need to place the default key file into .git/git-crypt/keys/
then git crypt add-gpg-user aiyenggar@icloud.com
finally you can git crypt unlock

At this stage you can seamlessly lock and unlock without further steps. But if I need to rsync to an external drive in a way that the content is encrypted, then what should I do? Should I delete the .git-crypt folder? Also, what happens if I lose the default key file. What is it, really?

# git commands
 git reset --hard HEAD^ If you are removing multiple commits from the top, you can run git reset --hard HEAD~2 to remove the last two commits
https://sethrobertson.github.io/GitFixUm/fixup.html
A wonderful site with many useful commands.


# character set of files
file -I *.tex
clusterskf.tex:        text/x-tex; charset=us-ascii
metadissertation.tex:  text/x-tex; charset=iso-8859-1
philosophy.tex:        text/x-tex; charset=us-ascii
proposal.tex:          text/x-tex; charset=utf-8

iconv -f iso-8859-1 -t utf-8 < metadissertation.tex > m.tex
