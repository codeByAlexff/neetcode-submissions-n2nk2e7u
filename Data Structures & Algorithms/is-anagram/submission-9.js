class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {

        if (s.length != t.length) return false

        const res = new Map()

        for(const char of s){
            let key = char.split('').join('')
            res.set(key, (res.get(key)||0) + 1)
        }

        for (const char of t){
            if (!res.get(char)) return false
            else res.set(char, (res.get(char) - 1))
        }
        return true


    }
}
