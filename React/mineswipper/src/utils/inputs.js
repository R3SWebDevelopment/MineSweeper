export const onChangeInput = (evt, obj) => {
  obj.setState({
    [evt.target.name]: evt.target.value
  })
}
