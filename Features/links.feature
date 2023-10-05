Feature: Links

    Scenario Outline: Links should work
        Given we visit the url <url>
        Then all links on the page should be reachable

        Examples: Pages
            | url |
            | /en |
            | /cy |
