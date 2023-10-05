Feature: Cookies

    Scenario Outline: Accepting cookies
        Given we visit the url <url>
        When we accept the cookies
        Then the cookie banner should not be visible

        Examples: Pages
            | url |
            | /en |
