import React, { Component } from 'react';

class WebSocketTest extends Component {

    constructor(props) {
        super(props);

        this.state = {
            messages : []
        };
    }

    componentDidMount(){
        // this is an "echo" websocket service
        fetch('http://localhost:8000/game/hello')
            .then(response => console.log(response.json()));

        this.connection = new WebSocket('ws://localhost:8000/ws/game/lobby/');
        // listen to onmessage event
        this.connection.onmessage = evt => {
            // add the new message to state
            const data = JSON.parse(evt.data);
            const message = data['message'];
            this.setState({
                messages : this.state.messages.concat(message)
            })
        };

        // for testing purposes: sending to the echo service which will send it back back
        // setInterval( _ =>{
        //     this.connection.send( Math.random() )
        // }, 2000 )
    }

    render() {
        // slice(-5) gives us the five most recent messages
        return <ul>{ this.state.messages.slice(-5).map( (msg, idx) => <li key={'msg-' + idx }>{ msg }</li> )}</ul>;
    }
}

export default WebSocketTest;


