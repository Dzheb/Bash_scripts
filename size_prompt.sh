#!/bin/bash

get_size() {
    local path="$1"
    local size=$(du -h -s "$path" 2>/dev/null | cut -f1)
    echo $size
}

get_prompt() {
    echo  "next 10 items - enter 'y'"
    read -s next10
    if [[ $next10 == "y" ||  $next10 == "Y" ||  $next10 == "yes"||  $next10 == "Yes" ]]
     then return 0
     else return 1
    fi
}

items=$(ls -A)

result=()
res_sorted=()
for item in $items; do
    size=$(get_size "$item")
    result+=("$size $item")
done
IFS=$'\n' res_sorted=($(sort -rn <<<"${result[*]}")); unset IFS
# printf "%s\n" "${res_sorted[@]}"
declare -i count=0
for ((i=0;i<${#res_sorted[@]};++i)); do
    if [[ $count -le 9 ]]; then count=$((count+1)); else if ! get_prompt;then break; else count=1;fi fi
    echo -e "${res_sorted[$position]}"
    position=$((i+1))
done
#echo $count
#if ! get_prompt
#then count=0; echo $count
#fi
