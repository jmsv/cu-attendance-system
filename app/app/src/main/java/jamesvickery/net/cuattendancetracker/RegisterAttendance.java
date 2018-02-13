package jamesvickery.net.cuattendancetracker;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

import java.io.IOException;

import okhttp3.FormBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class RegisterAttendance extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        String eventId = "";
        Bundle extras = getIntent().getExtras();
        if (extras != null) {
            eventId = extras.getString("event_id");
        }

        setContentView(R.layout.activity_register_attendance);


//        AlertDialog.Builder builder = new AlertDialog.Builder(this);
//        builder.setTitle("this is the code thing");
//        builder.setPositiveButton("OK", new DialogInterface.OnClickListener() {
//            @Override
//            public void onClick(DialogInterface dialog, int which) {
//                finish();
//            }
//        });
//        builder.setMessage(eventId);
//        AlertDialog alert = builder.create();
//        alert.show();

        TextView textViewEventId = findViewById(R.id.textViewEventId);
        textViewEventId.setText("signing into: " + eventId);
    }

    boolean registerAttendancePost(String event_id) {
        OkHttpClient client = new OkHttpClient();

        RequestBody formBody = new FormBody.Builder()
                .add("user", "7000000")
                .add("event", event_id)
                .build();

        Request request = new Request.Builder()
                .url("https://cu-attendance.net/api/register-attendance")
                .post(formBody)
                .build();

        try {
            Response response = client.newCall(request).execute();

            if (response.code() == 200) return true;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return false;
    }
}
