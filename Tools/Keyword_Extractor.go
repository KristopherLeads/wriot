// This tool is used to count the keywords in a given URL.
// It works by fetching the HTML content, extracting the plaintext, and processing by converting to lowercase, removing special characters, filtering common stop words, and then filtering words of length<3.
// The output is N most frequent words.
// You ned to pass two command-line args - URL and number of keywords to return.
// Install dependency with get golang.org/x/net/html

package main







import (
	"fmt"
	"io"
	"net/http"
	"os"
	"regexp"
	"sort"
	"strings"

	"golang.org/x/net/html"
)





// WordCount represents a word and its frequency
type WordCount struct {
	Word  string
	Count int
}
