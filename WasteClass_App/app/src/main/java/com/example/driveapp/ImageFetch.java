package com.example.driveapp;

public class ImageFetch {

    private String name;
    private String photo;


    public ImageFetch(String name, String photo) {
        this.name = name;
        this.photo = photo;
    }

    public ImageFetch() {
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPhoto() {
        return photo;
    }

    public void setPhoto(String photo) {
        this.photo = photo;
    }
}
