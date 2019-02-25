import React, {Component} from 'react';
import './App.css';

class App extends Component {
  constructor(){
    super();
    this.state = {
      todos : [],
      checks: []
    }
  }
  update(e){
    if(e.key === 'Enter'){
      let newArray = this.state.todos;
      newArray.push(e.target.value);
      let newChecks = this.state.checks;
      newChecks.push(false);
      this.setState({todos: newArray, checks: newChecks});
      e.target.value = "";
    }
  }
  clear(e,val){
    let index = this.state.todos.indexOf(val);

    let newArray = this.state.todos;
    newArray.splice( index, 1 );

    let newChecks = this.state.checks;
    newChecks.splice( index, 1 );

    this.setState({todos: newArray, checks: newChecks});

  }
  check(e,val){

    let newArray = this.state.checks;
    let index = this.state.todos.indexOf(val);

    if(newArray[index] === false){
      newArray[this.state.todos.indexOf(val)] = true;
    }else{
      newArray[this.state.todos.indexOf(val)] = false;
    }
    this.setState({checks: newArray});
  }
  render() {
    let items = this.state.todos;
    let checks = this.state.checks
    return (
      <div>
        <h1>To Do List</h1>

        <ul id="list2" className="collection">
          {items.map((item,index) =>
         <Task
          key={index}
          value={item}
          clear={this.clear.bind(this)}
          check={this.check.bind(this)}
          isChecked={checks[index]}
        />)}
        </ul>

        <input type="text"
        placeholder="New element"
        onKeyPress={this.update.bind(this)}
        />
      </div>
    )
  }
}

class Task extends React.Component {
  constructor(){
    super();
    this.state = {
      className : 'collection-item'
    }
  }
  render(props){
    let ind = this.props.value;
    let cn = "";
    let ch = false;
    if(this.props.isChecked){
      cn = "collection-item checked grey lighten-1";
      ch = true;
    }else{
      cn = "collection-item";
      ch = false;
    }
    return (

      <li className={cn} >
        <label>
          <input 
            type="checkbox"
            className="filled-in"
            onChange={ (e) => this.props.check(e, ind) }
            checked={ch} />
          <span>{this.props.value}</span>
         </label>
        <i
          className="material-icons secondary-content" 
          onClick={ (e) => this.props.clear(e, ind) } >clear
        </i>
       
      </li>

    )
  }
}



export default App;
