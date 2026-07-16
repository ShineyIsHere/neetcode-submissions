
class Solution {
public:
    bool isAnagram(string s, string t) {
        char arr1, arr2;
        int n =0, m=0;
        sort(s.begin(),s.end());
        sort(t.begin(),t.end());
        if (s == t) return true;
        else return false;
        
    }
};
