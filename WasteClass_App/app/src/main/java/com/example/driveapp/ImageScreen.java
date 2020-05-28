package com.example.driveapp;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.squareup.picasso.Picasso;

public class ImageScreen extends AppCompatActivity {

    ImageView imageView2;
    TextView textView2;
    DatabaseReference ref;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_image_screen);

        imageView2 = findViewById(R.id.imageView2);
        textView2 = findViewById(R.id.textView2);

        ref = FirebaseDatabase.getInstance().getReference().child("image");

        String ImageKey = getIntent().getStringExtra("ImageKey");

        ref.child(ImageKey).addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {

                if (dataSnapshot.exists()){
                    String name = dataSnapshot.child("name").getValue().toString();
                    String photo = dataSnapshot.child("photo").getValue().toString();

                    Picasso.get().load(photo).into(imageView2);
                    textView2.setText(name);
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });

    }
}
