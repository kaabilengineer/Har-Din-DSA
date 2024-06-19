// Day 3 leetcode
// KID with max candies
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
         List<Boolean>ans=new ArrayList<Boolean>();
         int maxi=Integer.MIN_VALUE;
         for(int i=0;i<candies.length;i++){
            if(candies[i]>maxi){
                maxi=candies[i];
            }
         }
         for(int i=0;i<candies.length;i++){
            if(candies[i]+extraCandies>=maxi){
                ans.add(i,true);
            }else ans.add(i,false);
         }
        return ans;
    }
}
