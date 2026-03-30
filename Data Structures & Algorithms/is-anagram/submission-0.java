class Solution {
    public boolean isAnagram(String s, String t) {

        int [] arr = new int[26];
        char [] s1 = s.toCharArray();

        char [] s2 = t.toCharArray();
        if(s.length()!= t.length()){
            return false;
        }
        for(char c : s1){
            arr[c-'a'] ++;
        }
        for(char c : s2){
            if(arr[c-'a']  == 0){
                return false;
            }
            else {
                arr[c-'a'] --;
            }
        }


        

        return true;
        
    }

}
