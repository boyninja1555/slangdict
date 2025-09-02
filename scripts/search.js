const searchResults = window.searchResults || []
const queryParams = new URLSearchParams(window.location.search)
const query = (queryParams.get("query") || "").trim().toLowerCase().split(" ")

if (!query[0]) {
    console.log(queryParams.getAll())
    window.location.href = "/"
}

let foundResults = []

searchResults.forEach(result => {
    const wordParts = result.trim().toLowerCase().split(" ")
    console.log(wordParts, query)

    if (query.some(q => wordParts.includes(q))) {
        foundResults.push(result)
    }

    console.warn(foundResults)
})

const target = foundResults.length > 0 ? foundResults[0] : "not-found"
window.location.href = `/words/${encodeURIComponent(target)}.html`
