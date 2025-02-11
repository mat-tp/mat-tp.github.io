function launchProject(project) {
    
    fetch(`/launch/${project}`).then(response => {
        if (response.ok) {
            // Handle the success, maybe redirect or display the URL
            response.json().then(data => {
                // Redirect to the public URL of the app
                window.location.href = data.url;
            });
        } else {
            alert('Failed to launch project.');
        }
    });
}
