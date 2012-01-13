function channels(network){

    var url ="/get_channels/" + network;

    $.get(url, function(data){
	    $( "#channels_list" ).empty().append(data);
	}
	);
}

function programs(channel){

    var url ="/get_programs/" + channel;

    $.get(url, function(data){
	    $( "#programs_list" ).empty().append(data);
	}
	);
}
function videos(program){

    var url ="/get_videos/" + program;

        $.get(url, function(data){
    	    $( "#videos_list" ).empty().append(data);
    	}
    	);
}


function fav(program_name){

    var url = "/fav/" + program_name;
    $.get(url,function(data){
    	    if (data == "OK"){
    		$("#favprogs").append('<li onclick="javascript:videos(\"'+program_name+'\")">'+program_name+'<li>');
    	    }
    	}
    	);
}

function like(video_name,program_name,episode_number){

    var url = "/like/" + video_name;
    var ok = "<li onclick=\"javascript:video('"+program_name+"','"+episode_number+"'); \">" +video_name +"</li>";
    $.get(url,function(data){
    	    if (data == "OK"){
		
    		$("#likedvideos").append(ok);
    	    }
    	}
    	);
}



function video(program_name, episode_number, video_name){
    var url="/episode/" + program_name + "/" + episode_number;
    $.get(url, function(data){
	    $( "#video").empty().append(data);
	}
	);


    $("#favlikebox").empty();
   

    var fav = "<div onclick=\"javascript:fav('"+program_name+"'); \">Add "+program_name+" to your favourites</div>";
    var like = "<div onclick=\"javascript:like('"+video_name+"','"+program_name+"','"+episode_number+"'); \">like this episode</div>";


    $("#favlikebox").append(fav);

    $("#favlikebox").append(like);

    //   $("#favlikebox").empty().append('<a href="/fav/'+program_name+'">fav</a><a href="/like/'+video_name+'">like</a>');
    // $("#favlikebox").append('<span onclick="javascript:console.log(\"ahmet\");fav(\"'+program_name+'\");">fav</span>');
    //$("#favlikebox").append('<span onclick="javascript:like(\"'+video_name+'\");">like</span>');
    
   
    
    $("#favlikebox").show();
}
