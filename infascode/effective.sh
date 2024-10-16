# shellcheck disable=SC2148
effective() {

    local filename
    local search_term

    if test "$#" -eq 0 || test "$#" -gt 2; then
        echo "Usage: effective [search_term] filename" >&2
        return 1
    fi

    if test "$#" -eq 1; then
        filename="$1"
        search_term=".*"
    else
        search_term="$1"
        filename="$2"
    fi

    if test ! -r "$filename" -a -f "$filename"; then
        echo "Error: File '$filename' not found or not readable." >&2
        return 2
    fi
    grep -v '^ *#' "$filename" | grep -i "$search_term"
}

# -v '^\s*#'
# '^[[:blank:]]*[^#[:blank:]]'
# -v '^ *#'
