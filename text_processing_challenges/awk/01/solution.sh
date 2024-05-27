awk '{avg=($2+$3+$4)/3; print $0,":",(avg<50)?"FAIL":(avg>=80)?"A":(avg>=60)?"B":"C";}' sample_input.txt
