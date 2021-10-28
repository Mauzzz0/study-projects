package com.mirea.semak.myapplicatio;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private TextView tvOut;
    private Button btnOK;
    private Button btnCancel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        tvOut = findViewById(R.id.tvOut);
        btnOK = findViewById(R.id.btnOk);
        btnCancel = findViewById(R.id.btnCancel);
        btnOK.setText("OK");
        btnCancel.setText("CANCEL");

        View.OnClickListener oclBtnOk = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tvOut.setText("Нажата ОК");
            }
        };

        View.OnClickListener oclBtnCancel = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tvOut.setText("Нажата CANCEL");
            }
        };

        btnOK.setOnClickListener(oclBtnOk);
        btnCancel.setOnClickListener(oclBtnCancel);
    }
}