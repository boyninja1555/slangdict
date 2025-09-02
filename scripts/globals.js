document.addEventListener("DOMContentLoaded", () => {
    const links = document.querySelectorAll("a")
    links.forEach(link => {
        let prefetchTimer
        link.addEventListener("mouseover", () => {
            prefetchTimer = setTimeout(() => {
                const href = link.href

                if (href && !document.querySelector(`link[href="${href}"][rel="prefetch"]`)) {
                    const prefetchLink = document.createElement("link")
                    prefetchLink.rel = "prefetch"
                    prefetchLink.href = href
                    document.head.appendChild(prefetchLink)
                    console.log(`Prefetching ${href}`)
                }
            }, 300)
        })
        link.addEventListener("mouseout", () => clearTimeout(prefetchTimer))
    })
})
