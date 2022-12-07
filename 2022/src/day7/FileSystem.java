package day7;

import java.util.Comparator;
import java.util.List;

public class FileSystem {

    // Members
    private final DirectoryNode root;
    private DirectoryNode current;
    private static final Integer diskSize = 70000000;

    // Constructors
    public FileSystem(){
        this.root = new DirectoryNode("/");
        this.current = this.root;
    }

    // Accessors
    public List<DirectoryNode> listDirectories(){
        return this.root.getDirectoryList();
    }

    // Mutators
    public void cd(String destination){
        switch (destination) {
            case ".." -> this.current = current == root ? root : current.getParent();
            case "/" -> this.current = this.root;
            default -> this.current = (DirectoryNode) this.current.getChildren().get(destination);
        }
    }

    public void addFile(String name, Integer size){
        this.current.addChild(new FileNode(name, size));
    }

    public void addDirectory(String name){
        this.current.addChild(new DirectoryNode(name, this.current));
    }

    public Integer findDirectoryToDelete(Integer neededSpace){
        Integer currentFreeSpace = diskSize - this.root.getSize();
        Integer memoryDeficit = neededSpace - currentFreeSpace;
        return this.listDirectories().stream()
                .sorted(Comparator.comparingInt(DirectoryNode::getSize))
                .filter(directoryNode -> directoryNode.getSize()>=memoryDeficit)
                .findFirst().get().getSize();
    }


}
