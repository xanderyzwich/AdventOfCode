package day7;

public abstract class FileSystemNode {

    // Members
    protected String name;

    // Constructors
    FileSystemNode(String name){
        this.name = name;
    }

    // Accessors
    public abstract Integer getSize();

    // Mutators
}
