
import java.util.ArrayList;
import java.util.List;


public class Tries {

    public static void main(String[] args) {
        final List<String> setOfStrings = new ArrayList<>();
        setOfStrings.add("pqrs");
        setOfStrings.add("pprt");
        setOfStrings.add("psst");
        setOfStrings.add("qqrs");
        setOfStrings.add("pqrs");
        Trie trie = new Trie();
        setOfStrings.forEach(trie::insert);

        trie.print(  trie.query("psst") );
        trie.print(  trie.query("psst") );
    }
}

class TrieNode{
    int terminating ;   // How many strings end to this node in tree
    final TrieNode[] trieNodes = new TrieNode[26];  // array for all letter of alphabet

    public TrieNode next(final char c){
        return trieNodes[c - 'a'];
    }
}

class Trie {

    final TrieNode root;
    public Trie() {

        this.root = new TrieNode();
    }

    public int query(String s) {
        TrieNode current = root;

        for (int i=0; i < s.length(); i++) {
            if (current == null || current.next(s.charAt(i)) == null ){
                return 0 ;
            }
            else current = current.next(s.charAt(i));
        }
        return current.terminating ;
    }

    public void insert (final String s) {
        TrieNode current = root;
        for (int i =0; i < s.length(); i++ ) {
            if (current.trieNodes[s.charAt(i) - 'a'] == null ) {
                current.trieNodes[s.charAt(i) - 'a'] = new TrieNode();
            }
            current = current.next(s.charAt(i));
        }
        current.terminating++;
    }

    public void delete(String s){
        TrieNode current = root;
        for (int i=0; i < s.length(); i++) {
            if (current == null ){
                throw new RuntimeException("String doesn't exist");
            }
            current = current.next(s.charAt(i));
        }
        current.terminating-- ;
    }

    public void update (final String old, final String newString ){
         delete(old);
         insert(newString);
    }

    public void print(int result){

        if ( result == 0 ) {
            System.out.println(" String does NOTexist");
        }
        else System.out.println("String exist");
    }


}