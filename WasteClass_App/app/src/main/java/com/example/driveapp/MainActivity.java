package com.example.driveapp;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.load.model.ModelLoader;
import com.firebase.ui.database.FirebaseRecyclerAdapter;
import com.firebase.ui.database.FirebaseRecyclerOptions;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.storage.FileDownloadTask;
import com.google.firebase.storage.FirebaseStorage;
import com.google.firebase.storage.StorageReference;
import com.squareup.picasso.Picasso;

import java.io.File;
import java.io.IOException;

public class MainActivity extends AppCompatActivity {

//    ImageView image;
//    Button button;
    FloatingActionButton button;
    RecyclerView recyclerView;
    FirebaseRecyclerOptions<ImageFetch> options;
    FirebaseRecyclerAdapter<ImageFetch, MyViewHolder>adapter;
    DatabaseReference Dataref;
    TextView tv;
    TextView tv2;


//    FirebaseStorage storage = FirebaseStorage.getInstance();
//    StorageReference storageReference = storage.getReferenceFromUrl("gs://wasteclassifier-2c0bc.appspot.com/photos").child("pic1.jpg");


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

//        image = findViewById(R.id.image);
        button = findViewById(R.id.button);
        recyclerView = findViewById(R.id.recyclerView);
        tv = findViewById(R.id.tv);
        tv2 = findViewById(R.id.tv2);

        LinearLayoutManager layoutManager = new LinearLayoutManager(getApplicationContext());
        layoutManager.setReverseLayout(true);
        layoutManager.setStackFromEnd(true);
        recyclerView.setLayoutManager(layoutManager);
//        recyclerView.setLayoutManager(new LinearLayoutManager(getApplicationContext()));
//        recyclerView.setHasFixedSize(true);

        Dataref = FirebaseDatabase.getInstance().getReference().child("image");

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                LoadData();
            }
        });


        LoadData();


    }

    private void LoadData() {

        options = new FirebaseRecyclerOptions.Builder<ImageFetch>().setQuery(Dataref, ImageFetch.class).build();
        adapter = new FirebaseRecyclerAdapter<ImageFetch, MyViewHolder>(options) {
            @Override
            protected void onBindViewHolder(@NonNull MyViewHolder holder, int position, @NonNull ImageFetch model) {

                holder.textView.setText(model.getName());
                Picasso.get().load(model.getPhoto()).into(holder.imageView);

                holder.v.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        Intent intent = new Intent(MainActivity.this, ImageScreen.class);
                        intent.putExtra("ImageKey", getRef(position).getKey());
                        startActivity(intent);
                    }
                });


            }

            @NonNull
            @Override
            public MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {

                View v = LayoutInflater.from(parent.getContext()).inflate(R.layout.single_view, parent, false);
                return new MyViewHolder(v);
            }

            @Override
            public void onDataChanged() {
                super.onDataChanged();

                adapter.notifyDataSetChanged();
                Integer i  = adapter.getItemCount();
                tv.setText(Integer.toString(i));
            }

        };


        adapter.startListening();
        recyclerView.setAdapter(adapter);





    }

//        button.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                try{
//                    final File file = File.createTempFile("image", "jpg");
//                    storageReference.getFile(file).addOnSuccessListener(new OnSuccessListener<FileDownloadTask.TaskSnapshot>() {
//                        @Override
//                        public void onSuccess(FileDownloadTask.TaskSnapshot taskSnapshot) {
//                            Bitmap bitmap = BitmapFactory.decodeFile(file.getAbsolutePath());
////                            image.setImageBitmap(bitmap);
//
//                        }
//                    }).addOnFailureListener(new OnFailureListener() {
//                        @Override
//                        public void onFailure(@NonNull Exception e) {
//                            Toast.makeText(MainActivity.this, "Image Failed To Load", Toast.LENGTH_SHORT).show();
//                        }
//                    });
//                } catch (IOException e) {
//                    e.printStackTrace();
//                }
//            }
//        });
//

        }

