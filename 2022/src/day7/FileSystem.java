package day7;

import java.util.Comparator;
import java.util.List;

public class FileSystem {

    // Members
    private DirectoryNode root;
    private DirectoryNode current;
    private Integer diskSize = 70000000;
    private Integer neededSpace = 30000000;

    // Constructors
    public FileSystem(){
        this.root = new DirectoryNode("/");
        this.current = this.root;
    }

    // Accessors
    public List<DirectoryNode> listDirectories(){
        List<DirectoryNode> directoryList = this.root.getDirectoryList();
//        System.out.println(directoryList);
        return directoryList;
    }

    // Mutators
    public void cd(String destination){
        String where = destination.equals("..") ? "up to " +this.current.parent.name : destination;
//        System.out.printf("Changing Directory %s%n", where);
        switch (destination) {
            case ".." -> this.current = current == root ? root : current.parent;
            case "/" -> this.current = this.root;
            default -> this.current = (DirectoryNode) this.current.children.get(destination);
        }
    }

    public void addFile(String name, Integer size){
        String here = this.current.name.equals("/") ? "" : this.current.name;
//        System.out.printf("Adding file %s/%s: %s%n", here, name, size);
        this.current.addChild(new FileNode(name, size));
    }

    public void addDirectory(String name){
        String here = this.current.name.equals("/") ? "" : this.current.name;
//        System.out.printf("Adding directory %s/%s%n", here, name);
        this.current.addChild(new DirectoryNode(name, this.current));
    }

    public Integer findDirectoryToDelete(){
        Integer currentFreeSpace = this.diskSize - this.root.getSize();
        Integer memoryDeficit = this.neededSpace - currentFreeSpace;
        return this.listDirectories().stream()
                .sorted(Comparator.comparingInt(DirectoryNode::getSize))
                .filter(directoryNode -> directoryNode.getSize()>=memoryDeficit)
                .findFirst().get().getSize();
    }


}
