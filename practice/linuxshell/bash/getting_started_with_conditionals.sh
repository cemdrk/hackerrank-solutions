read ans

# case "$ans" in
#     [yY])
#         echo YES
#         ;;
#     [nN])
#         echo NO
#         ;;
# esac

if [[ $ans == "y" || $ans == "Y"  ]]; then
     echo YES
elif [[ $ans == "n" || $ans == "N"  ]]; then
     echo NO
fi
