import React, { Component } from "react";


class SearchBar extends Component {
  render(){
    return(
      <div className='search'>
        <input placeholder='Search' onChange={this.props.onChange}/>
      </div>
    )
  }
}

export default class People extends Component {
  constructor(props){
    super(props);
    this.state ={
      people : [],
      search_list : [],
      search_term : '',
    }
  }

  renderPerson(lst){
    for (let i=0; i<lst.length; i++){
      return (lst.map((key) => (<div className="displaydiv" key={key.phone_number}><div className="personname">{key.name}</div><div className="personnumber">{key.phone_number}</div></div>)))
    }
  }

  componentDidMount(){
    // console.log("hi");
    let my_list = [];
    fetch('/people_list/', {
  credentials: 'include'
} ).then((response) => response.json()).then((data) => {
      for (let i=0; i<data.length; i++){
        my_list.push(data[i]);
      }
      this.setState({
        people: my_list,
        search_list: my_list
      })
      // console.log(data);
      console.log(this.state.search_list);
    })
  }

  update_search(){
    let searched_list = this.state.people.filter(person => (person.name).toLowerCase().includes(this.state.search_term.toLowerCase()))
    this.setState({
      search_list: searched_list
    })
    console.log(this.state.search_list);
  }

  searcher = (e) => {
    console.log(e.target.value);
    this.setState({
      search_term: e.target.value
    })
    this.update_search();
  }


  render(){
    return(
      <div className="People">
        <SearchBar value={this.state.searchterm} onChange={this.searcher} placeholder="search me"/>
        <div>
          <ul>
            {this.renderPerson([{ id:0, name:"Usernames", phone_number:"Phone Numbers"}])}
            {this.renderPerson(this.state.search_list)}
          </ul>
        </div>
      </div>
    )
  }

}
