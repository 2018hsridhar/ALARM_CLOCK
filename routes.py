from flask import Blueprint, jsonify, render_template, request, current_app

main = Blueprint('main', __name__)

# This file defines the routes for the Flask application.
# The routes handle various HTTP requests and interact with the application logic.

@main.route('/', methods=['GET'])
def index():
    return render_template('home.html')
    
@main.route('/health', methods=['GET'])
def health_check():
    return jsonify(status="ok"), 200

# @main.route('/hello', methods=['GET'])
# def hello_world():
#     return render_template('hello.html')

# # APIs - return only JSON data, or also render HTML templates?
# # JSON - programatic desireable
# # curl -X GET http://localhost:5000/getUserBase
# @main.route('/getUserBase', methods=['GET'])
# def get_user_base():
#     my_user_base = current_app.my_user_song_app.get_user_base()
#     if not my_user_base:
#         return jsonify(error="User base is empty"), 404
#     # return jsonify(songs=my_user_base), 200
#     user_base_payload = {"users": my_user_base}
#     return render_template('primary_data_display.html', payload=user_base_payload)

# # Unit testing : 
# # curl -X POST -H "Content-Type: application/json" -d '{"user": "Natalie"}' http://localhost:5000/addUser
# @main.route('/addUser', methods=['POST'])
# def add_a_user():
#     my_user_base = current_app.my_user_song_app.my_user_base
#     data = request.get_json()
#     user = data.get('user', None)
#     if not user or not isinstance(user, str):
#         return jsonify(error="Invalid user input"), 400
#     my_user_base.append(user)
#     # In a real application, you would handle the update logic here
#     # For this example, we will just return a success message
#     success_message = "User list updated successfully"
#     return jsonify(message=success_message), 200

# # curl -X DELETE -H "Content-Type: application/json" -d '{"user": "Sophia"}' http://localhost:5000/deleteUser
# @main.route('/deleteUser', methods=['DELETE'])
# def delete_user():
#     my_user_base = current_app.my_user_song_app.my_user_base
#     data = request.get_json()
#     user = data.get('user', None)
#     if not user or not isinstance(user, str):
#         return jsonify(error="Invalid user input"), 400
#     if user in my_user_base:
#         my_user_base.remove(user)
#         success_message = "User list updated successfully"
#         return jsonify(message=success_message), 200
#     else:
#         return jsonify(error="User not found"), 404

# # curl -X GET "http://localhost:5000/getMySongListByUserId?user_id=hari"
# @main.route('/getMySongListByUserId', methods=['GET'])
# def get_my_song_list():
#     data = request.args
#     user_id = data.get('user_id', None)
#     if not user_id or not isinstance(user_id, str):
#         return jsonify(error="Invalid user_id input"), 400
#     my_song_list = current_app.my_user_song_app.get_song_list_by_user_id(user_id)
#     songs_payload = {"songs": my_song_list}
#     return render_template('primary_data_display.html', payload=songs_payload)
#     # return jsonify(songs=my_song_list), 200

# # This route simulates updating the song list
# # Input should be a string representing the song to be added, passed in a JSON payload
# # Unit testing : curl -X POST -H "Content-Type: application/json" -d '{"user_id": "hari", "song": "New Song"}' http://localhost:5000/updateSongListByUserId
# @main.route('/updateSongListByUserId', methods=['POST'])
# def update_song_list_by_user_id():
#     data = request.get_json()
#     song = data.get('song', None)
#     user_id = data.get('user_id', None)
#     if not user_id or not isinstance(user_id, str):
#         return jsonify(error="Invalid user_id input"), 400
#     if not song or not isinstance(song, str):
#         return jsonify(error="Invalid song input"), 400
#     current_app.my_user_song_app.add_song_to_user(user_id, song)
#     print(current_app.my_user_song_app.user_songs)  # Debugging line to check the user songs
#     # In a real application, you would handle the update logic here
#     # For this example, we will just return a success message
#     success_message = "Song list updated successfully : for userID = {user_id}, added song = {song}"
#     return jsonify(message=success_message), 200

# # Testing = curl -X DELETE -H "Content-Type: application/json" -d '{"song": "New Song"}' http://localhost:5000/deleteASong
# @main.route('/deleteASongByUserId', methods=['DELETE'])
# def delete_a_song():
#     data = request.get_json()
#     song = data.get('song', None)
#     user_id = data.get('user_id', None)
#     if not user_id or not isinstance(user_id, str):
#         return jsonify(error="Invalid user_id input"), 400
#     if not song or not isinstance(song, str):
#         return jsonify(error="Invalid song input"), 400
#     try:
#         current_app.my_user_song_app.delete_song_from_user(user_id, song)
#         success_message = "Song list updated successfully : for userID = {user_id}, deleted song = {song}"
#         return jsonify(message=success_message),200
#     except ValueError:
#         return jsonify(error="Song not found in the list"), 404
