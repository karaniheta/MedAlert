import 'package:flutter/material.dart';

class AmbulanceScreen extends StatelessWidget {
  const AmbulanceScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.white,
        elevation: 0,
        iconTheme: const IconThemeData(color: Colors.black),
        title: const Text(
          'Hello Ideate !',
          style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold),
        ),
      ),
      body: Padding(
        padding: const EdgeInsets.all(
          24.0,
        ), // Increased padding for better spacing
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            // Ambulance Header
            Container(
              padding: const EdgeInsets.all(
                24,
              ), // Increased padding inside the header
              decoration: BoxDecoration(
                color: const Color(0xFF6C63FF),
                borderRadius: BorderRadius.circular(
                  16,
                ), // Slightly larger border radius
              ),
              child: const Center(
                child: Text(
                  'Ambulance',
                  style: TextStyle(
                    fontSize: 28, // Increased font size
                    fontWeight: FontWeight.bold,
                    color: Colors.white,
                  ),
                ),
              ),
            ),
            const SizedBox(height: 32), // Increased spacing between sections
            // Name Field
            const Text(
              'Name',
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ), // Slightly larger font size
            ),
            const SizedBox(height: 12), // Increased spacing
            TextField(
              decoration: InputDecoration(
                hintText: 'Narendra Modi',
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(
                    12,
                  ), // Larger border radius
                ),
              ),
            ),
            const SizedBox(height: 24), // Increased spacing
            // Phone Number Field
            const Text(
              'Phone no',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 12),
            TextField(
              decoration: InputDecoration(
                hintText: '+91 01234 56789',
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
              ),
            ),
            const SizedBox(height: 24),

            // Address Field
            const Text(
              'Address',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 12),
            TextField(
              maxLines: 5, // Increased max lines for better visibility
              decoration: InputDecoration(
                hintText:
                    'Sunshine Residency, Flat 302\n2nd Floor, Plot No. 56, Shanti Nagar\nNear Ganga Temple, Sector 12\nBangalore, Karnataka - 560078',
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
              ),
            ),
            const SizedBox(height: 24),

            // Detect from Profile Checkbox
            Row(
              children: [
                Checkbox(
                  value: false,
                  onChanged: (value) {
                    // TODO: Handle checkbox logic
                  },
                ),
                const Text(
                  'Detect from profile',
                  style: TextStyle(fontSize: 16),
                ),
              ],
            ),
            const Spacer(), // Pushes the button to the bottom of the screen
            // Book Now Button
            ElevatedButton(
              onPressed: () {
                // TODO: Handle booking logic
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: const Color(0xFF6C63FF),
                padding: const EdgeInsets.symmetric(
                  vertical: 20,
                ), // Larger button height
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
              ),
              child: const Text(
                'BOOK NOW',
                style: TextStyle(
                  fontSize: 20, // Larger font size
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
