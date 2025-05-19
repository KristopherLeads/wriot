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

// Common stop words to filter out
var stopWords = map[string]bool{
	"a": true, "about": true, "above": true, "after": true, "again": true, "against": true, "all": true,
	"am": true, "an": true, "and": true, "any": true, "are": true, "as": true, "at": true, "be": true,
	"because": true, "been": true, "before": true, "being": true, "below": true, "between": true, "both": true,
	"but": true, "by": true, "can": true, "did": true, "do": true, "does": true, "doing": true, "don": true,
	"down": true, "during": true, "each": true, "few": true, "for": true, "from": true, "further": true,
	"had": true, "has": true, "have": true, "having": true, "he": true, "her": true, "here": true, "hers": true,
	"herself": true, "him": true, "himself": true, "his": true, "how": true, "i": true, "if": true, "in": true,
	"into": true, "is": true, "it": true, "its": true, "itself": true, "just": true, "me": true, "more": true,
	"most": true, "my": true, "myself": true, "no": true, "nor": true, "not": true, "now": true, "of": true,
	"off": true, "on": true, "once": true, "only": true, "or": true, "other": true, "our": true, "ours": true,
	"ourselves": true, "out": true, "over": true, "own": true, "same": true, "she": true, "should": true,
	"so": true, "some": true, "such": true, "than": true, "that": true, "the": true, "their": true, "theirs": true,
	"them": true, "themselves": true, "then": true, "there": true, "these": true, "they": true, "this": true,
	"those": true, "through": true, "to": true, "too": true, "under": true, "until": true, "up": true,
	"very": true, "was": true, "we": true, "were": true, "what": true, "when": true, "where": true, "which": true,
	"while": true, "who": true, "whom": true, "why": true, "will": true, "with": true, "you": true, "your": true,
	"yours": true, "yourself": true, "yourselves": true,
}

func main() {
	if len(os.Args) != 3 {
		fmt.Println("Usage: program <url> <number_of_keywords>")
		os.Exit(1)
	}

	url := os.Args[1]
	numKeywords := 0
	fmt.Sscanf(os.Args[2], "%d", &numKeywords)

	if numKeywords <= 0 {
		fmt.Println("Number of keywords must be greater than 0")
		os.Exit(1)
	}

	// Fetch the webpage content
	content, err := fetchURL(url)
	if err != nil {
		fmt.Printf("Error fetching URL: %v\n", err)
		os.Exit(1)
	}

	// Extract text from HTML
	text, err := extractTextFromHTML(content)
	if err != nil {
		fmt.Printf("Error extracting text: %v\n", err)
		os.Exit(1)
	}

	// Extract keywords
	keywords := extractKeywords(text, numKeywords)

	// Print results
	fmt.Printf("Top %d keywords from %s:\n", numKeywords, url)
	fmt.Println("----------------------------------")
	for i, kw := range keywords {
		fmt.Printf("%d. %s (%d occurrences)\n", i+1, kw.Word, kw.Count)
	}
}

// fetchURL retrieves the content of a URL
func fetchURL(url string) (string, error) {
	resp, err := http.Get(url)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return "", fmt.Errorf("HTTP request failed with status code: %d", resp.StatusCode)
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", err
	}

	return string(body), nil
}

// extractTextFromHTML extracts plain text from HTML content
func extractTextFromHTML(htmlContent string) (string, error) {
	doc, err := html.Parse(strings.NewReader(htmlContent))
	if err != nil {
		return "", err
	}

	var textParts []string
	var extractText func(*html.Node)
	extractText = func(n *html.Node) {
		if n.Type == html.TextNode {
			text := strings.TrimSpace(n.Data)
			if text != "" {
				textParts = append(textParts, text)
			}
		}
		for c := n.FirstChild; c != nil; c = c.NextSibling {
			// Skip script and style elements
			if c.Type == html.ElementNode && (c.Data == "script" || c.Data == "style") {
				continue
			}
			extractText(c)
		}
	}
	extractText(doc)

	return strings.Join(textParts, " "), nil
}

// extractKeywords extracts and counts keywords from text
func extractKeywords(text string, numKeywords int) []WordCount {
	// Convert to lowercase
	text = strings.ToLower(text)

	// Remove special characters and replace with spaces
	re := regexp.MustCompile(`[^a-z0-9\s]`)
	text = re.ReplaceAllString(text, " ")

	// Split into words
	words := strings.Fields(text)

	// Count word frequencies
	wordFreq := make(map[string]int)
	for _, word := range words {
		// Skip short words (likely not meaningful keywords)
		if len(word) < 3 {
			continue
		}

		// Skip common stop words
		if stopWords[word] {
			continue
		}

		wordFreq[word]++
	}

	// Convert map to slice for sorting
	var wordCounts []WordCount
	for word, count := range wordFreq {
		wordCounts = append(wordCounts, WordCount{Word: word, Count: count})
	}

	// Sort by frequency (descending)
	sort.Slice(wordCounts, func(i, j int) bool {
		return wordCounts[i].Count > wordCounts[j].Count
	})

	// Return top N keywords
	if len(wordCounts) > numKeywords {
		wordCounts = wordCounts[:numKeywords]
	}

	return wordCounts
}
