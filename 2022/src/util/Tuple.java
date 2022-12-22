package util;

import lombok.AllArgsConstructor;
import lombok.Data;

import static java.lang.Math.pow;

@Data
@AllArgsConstructor
public class Tuple <T, V> {
    private T first;
    private V second;

    @Override
    public boolean equals(Object obj){
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Tuple<T, V> other = (Tuple<T, V>) obj;
        return this.first.equals(other.first) && this.second.equals(other.second);
    }
    @Override
    public int hashCode(){
        int lengthOfFirst = Integer.valueOf(this.first.hashCode()).toString().length();
        final int offset = (int) pow(10, lengthOfFirst);
        return (this.first.hashCode()*offset) + this.second.hashCode();
    }
    @Override
    public String toString(){
        return "(%s, %s)".formatted(this.first, this.second);
    }

}
