package day7;

import lombok.Getter;

@Getter
public abstract class FileSystemNode {

    // Members
    private final String name;

    // Constructors
    FileSystemNode(String name){
        this.name = name;
    }

    // Accessors
    public abstract Integer getSize();

    // Mutators
}
