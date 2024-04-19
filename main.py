import click


# Dictionary to store menu options and their corresponding actions

menu_options = {
            'Array': {
                'Two Sum': 'https://leetcode.com/problems/two-sum/',
                'Best Time to Buy and Sell Stock': 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock/',
                'Contains Duplicate': 'https://leetcode.com/problems/contains-duplicate/',
                'Product of Array Except Self': 'https://leetcode.com/problems/product-of-array-except-self/',
                'Maximum Subarray': 'https://leetcode.com/problems/maximum-subarray/',
                'Maximum Product Subarray': 'https://leetcode.com/problems/maximum-product-subarray/',
                'Find Minimum in Rotated Sorted Array': 'https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/',
                'Search in Rotated Sorted Array': 'https://leetcode.com/problems/search-in-rotated-sorted-array/',
                '3 Sum': 'https://leetcode.com/problems/3sum/',
                'Container With Most Water': 'https://leetcode.com/problems/container-with-most-water/'
            },
            'Binary': {
                'Sum of Two Integers': 'https://leetcode.com/problems/sum-of-two-integers/',
                'Number of 1 Bits': 'https://leetcode.com/problems/number-of-1-bits/',
                'Counting Bits': 'https://leetcode.com/problems/counting-bits/',
                'Missing Number': 'https://leetcode.com/problems/missing-number/',
                'Reverse Bits': 'https://leetcode.com/problems/reverse-bits/'
            },
            'Dynamic Programming': {
                'Climbing Stairs': 'https://leetcode.com/problems/climbing-stairs/',
                'Coin Change': 'https://leetcode.com/problems/coin-change/',
                'Longest Increasing Subsequence': 'https://leetcode.com/problems/longest-increasing-subsequence/',
                'Longest Common Subsequence': 'https://leetcode.com/problems/longest-common-subsequence/',
                'Word Break Problem': 'https://leetcode.com/problems/word-break/',
                'Combination Sum': 'https://leetcode.com/problems/combination-sum/',
                'House Robber': 'https://leetcode.com/problems/house-robber/',
                'House Robber II': 'https://leetcode.com/problems/house-robber-ii/',
                'Decode Ways': 'https://leetcode.com/problems/decode-ways/',
                'Unique Paths': 'https://leetcode.com/problems/unique-paths/',
                'Jump Game': 'https://leetcode.com/problems/jump-game/'
            },
            'Graph': {
                'Clone Graph': 'https://leetcode.com/problems/clone-graph/',
                'Course Schedule': 'https://leetcode.com/problems/course-schedule/',
                'Pacific Atlantic Water Flow': 'https://leetcode.com/problems/pacific-atlantic-water-flow/',
                'Number of Islands': 'https://leetcode.com/problems/number-of-islands/',
                'Longest Consecutive Sequence': 'https://leetcode.com/problems/longest-consecutive-sequence/'
            },
            'Interval': {
                'Insert Interval': 'https://leetcode.com/problems/insert-interval/',
                'Merge Intervals': 'https://leetcode.com/problems/merge-intervals/',
                'Non-overlapping Intervals': 'https://leetcode.com/problems/non-overlapping-intervals/'
            },
            'Linked List': {
                'Reverse a Linked List': 'https://leetcode.com/problems/reverse-linked-list/',
                'Detect Cycle in a Linked List': 'https://leetcode.com/problems/linked-list-cycle/',
                'Merge Two Sorted Lists': 'https://leetcode.com/problems/merge-two-sorted-lists/',
                'Merge K Sorted Lists': 'https://leetcode.com/problems/merge-k-sorted-lists/',
                'Remove Nth Node From End Of List': 'https://leetcode.com/problems/remove-nth-node-from-end-of-list/',
                'Reorder List': 'https://leetcode.com/problems/reorder-list/'
            },
            'Matrix': {
                'Set Matrix Zeroes': 'https://leetcode.com/problems/set-matrix-zeroes/',
                'Spiral Matrix': 'https://leetcode.com/problems/spiral-matrix/',
                'Rotate Image': 'https://leetcode.com/problems/rotate-image/',
                'Word Search': 'https://leetcode.com/problems/word-search/'
            },
            'String': {
                'Longest Substring Without Repeating Characters': 'https://leetcode.com/problems/longest-substring-without-repeating-characters/',
                'Longest Repeating Character Replacement': 'https://leetcode.com/problems/longest-repeating-character-replacement/',
                'Minimum Window Substring': 'https://leetcode.com/problems/minimum-window-substring/',
                'Valid Anagram': 'https://leetcode.com/problems/valid-anagram/',
                'Group Anagrams': 'https://leetcode.com/problems/group-anagrams/',
                'Valid Parentheses': 'https://leetcode.com/problems/valid-parentheses/',
                'Valid Palindrome': 'https://leetcode.com/problems/valid-palindrome/',
                'Longest Palindromic Substring': 'https://leetcode.com/problems/longest-palindromic-substring/',
                'Palindromic Substrings': 'https://leetcode.com/problems/palindromic-substrings/'
            },
            'Tree': {
                'Maximum Depth of Binary Tree': 'https://leetcode.com/problems/maximum-depth-of-binary-tree/',
                'Same Tree': 'https://leetcode.com/problems/same-tree/',
                'Invert/Flip Binary Tree': 'https://leetcode.com/problems/invert-binary-tree/',
                'Binary Tree Maximum Path Sum': 'https://leetcode.com/problems/binary-tree-maximum-path-sum/',
                'Binary Tree Level Order Traversal': 'https://leetcode.com/problems/binary-tree-level-order-traversal/',
                'Serialize and Deserialize Binary Tree': 'https://leetcode.com/problems/serialize-and-deserialize-binary-tree/',
                'Subtree of Another Tree': 'https://leetcode.com/problems/subtree-of-another-tree/',
                'Construct Binary Tree from Preorder and Inorder Traversal': 'https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/',
                'Validate Binary Search Tree': 'https://leetcode.com/problems/validate-binary-search-tree/',
                'Kth Smallest Element in a BST': 'https://leetcode.com/problems/kth-smallest-element-in-a-bst/',
                'Lowest Common Ancestor of BST': 'https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/',
                'Implement Trie (Prefix Tree)': 'https://leetcode.com/problems/implement-trie-prefix-tree/',
                'Add and Search Word': 'https://leetcode.com/problems/add-and-search-word-data-structure-design/',
                'Word Search II': 'https://leetcode.com/problems/word-search-ii/'
            },
            'Heap': {
                'Merge K Sorted Lists': 'https://leetcode.com/problems/merge-k-sorted-lists/',
                'Top K Frequent Elements': 'https://leetcode.com/problems/top-k-frequent-elements/',
                'Find Median from Data Stream': 'https://leetcode.com/problems/find-median-from-data-stream/'
            }
        
    }



state = []
def display_menu(menu):
    click.secho("\nChoose an option:", fg="blue")
    for index, option in enumerate(menu, start=1):
        click.echo(f"{index}. {option}")

def get_choice(menu):
    choice = click.prompt("Enter your choice [0 for back, -1 for exit]", type=int, default=0)
    if -1 <= choice <= len(menu):
        return choice
    else:
        click.secho("\nInvalid choice. Please try again.", fg="red")
        return get_choice(menu)

def navigate_menu(menu, state):
    click.secho("  Welcome to Blind75  ",fg="black",bg="green",bold=True)
    display_menu(menu)
    choice = get_choice(menu)
    if choice == -1:
        click.secho("\nBye...", fg="green")
        exit()
    elif choice == 0:  # Go back option
        if len(state) != 0:
            previous_menu = state.pop()
            navigate_menu(previous_menu, state)
        else:
            click.secho("\nYou are already at the top level.", fg="yellow")
            navigate_menu(menu, state)
    elif 1 <= choice <= len(menu):
        selected_option = list(menu.keys())[choice - 1]
        if isinstance(menu[selected_option], dict):
            state.append(menu)
            navigate_menu(menu[selected_option], state)
        else:
            click.secho(f"\nYou selected: {selected_option}", fg="white")
            click.secho(f"Problem link: ")
            click.secho(f"{menu[selected_option]}",fg="green")
            navigate_menu(menu, state)
    else:
        click.secho("\nInvalid choice. Please try again.", fg="red")
        navigate_menu(menu, state)


if __name__ == "__main__":
    navigate_menu(menu_options, state)