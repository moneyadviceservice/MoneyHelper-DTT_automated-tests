Feature: Components

    Scenario Outline: Emergency banner
        Given we visit the url <url>
        When we accept the cookies
        And we dismiss the emergency banner
        And we refresh the page
        Then the emergency banner should not be visible

        Examples: Pages
            | url |
            | /en |

    Scenario Outline: Header Search
        Given we visit the url <url>
        When we enter the search term <term> into the header search
        Then we should reach the search results page with the title <expected_search_title>

        Examples: Pages
            | url | term    | expected_search_title        |
            | /en | Housing | Search results for           |
            | /cy | Biliau  | Canlyniadau chwilio ar gyfer |

    Scenario Outline: Share this article - email
        Given we visit the url <url>
        When we accept the cookies
        And we expand the email panel
        Then we should be able to click the copy link button from the email panel

        Examples: Pages
            | url |
            | /en |
            | /cy |

    Scenario Outline: Share this article - more options
        Given we visit the url <url>
        When we accept the cookies
        And we expand the more options panel
        Then we should be able to click the copy link button from the more options panel

        Examples: Pages
            | url |
            | /en |
            | /cy |
