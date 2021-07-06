if grep -Fq "rc${PR_NUMBER}" ./gytrash/__about__.py
then
    echo "Release"
else
    echo "PR"
fi