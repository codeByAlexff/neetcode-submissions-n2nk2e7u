class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {

        //group map of [sortedWord, words equal to it]

        const group = {}

        for (const string of strs){
            let key = string.split('').sort().join('')
            if(!group[key]){
                group[key] = []
            }
            group[key].push(string)
        }
        return Object.values(group)
    }
}
