package day7;

public class FileNode extends FileSystemNode{

    // Members
    private final Integer size;

    // Constructors
    FileNode(String name, Integer size) {
        super(name);
        this.size = size;
    }

    // Accessors
    @Override
    public Integer getSize() {
        return this.size;
    }

    // Mutators
}
