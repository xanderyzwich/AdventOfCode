package day7;

import java.util.*;

public class DirectoryNode extends FileSystemNode{

    // members
    Map<String, FileSystemNode> children;
    DirectoryNode parent;

    // Constructors
    DirectoryNode(String name, DirectoryNode parent){
        super(name);
        this.parent = parent;
        this.children = new HashMap<>();
    }

    DirectoryNode(String name){
        this(name, null);
    }

    // Accessors
    @Override
    public Integer getSize() {
        return children.values().stream()
                .map(FileSystemNode::getSize)
                .reduce(0, Integer::sum);
    }

    List<DirectoryNode> getDirectoryList(){
        List<DirectoryNode> directoryNodeList = new LinkedList<>();
        directoryNodeList.add(this);
        this.children.values().stream()
                .filter(fileSystemNode -> fileSystemNode instanceof DirectoryNode)
                .map(dn -> (DirectoryNode)dn)
                .forEach(directoryNode -> directoryNodeList.addAll(directoryNode.getDirectoryList()));
//        System.out.printf("Listing directory %s: %s%n", this.name, directoryNodeList);
        return directoryNodeList;
    }

    public String toString(){
        return String.format("%s: %s", this.name, this.getSize());
    }

    // Mutators
    void addChild(FileSystemNode child){
        children.put(child.name, child);
    }
}
