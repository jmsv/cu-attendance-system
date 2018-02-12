package jamesvickery.net.cuattendancetracker;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

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
}
