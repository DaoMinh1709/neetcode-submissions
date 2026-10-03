class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> mark;
        for (int num: nums) {
            if (mark.count(num))
                return true;
            mark.insert(num);
        }
        return false;
    }
};