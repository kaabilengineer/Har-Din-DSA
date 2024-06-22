//Day 5 Bit manipulation

// 338. Counting Bits
class Solution {
    public int[] countBits(int n) {
        int[] re = new int[n+1];
        for (int i=1;i<=n;i++){
            re[i] = re[i>>1]+(i&1);
        }
        return re;
        
    }
}
