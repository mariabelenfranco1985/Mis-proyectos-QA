describe('Flujo principal del Banco', () => {
  
  it('Validar carga de la página inicial', () => {
    cy.visit('http://zero.webappsecurity.com/index.html')
    cy.title().should('include', 'Zero - Personal Banking') // validar título
    cy.get('#signin_button').should('be.visible') // validar botón visible
    cy.log('✅ Página de inicio cargada correctamente')
  })

  it('Ingresar al formulario de login', () => {
    cy.visit('http://zero.webappsecurity.com/index.html')
    cy.get('#signin_button').click()
    cy.url().should('include', 'login.html')
    cy.get('input#user_login').should('be.visible')
    cy.get('input#user_password').should('be.visible')
    cy.log('✅ Formulario de login visible')
  })

  it('Intentar iniciar sesión con credenciales incorrectas', () => {
    cy.visit('http://zero.webappsecurity.com/login.html')
    cy.get('input#user_login').type('usuario_invalido')
    cy.get('input#user_password').type('clave_invalida')
    cy.get('input[name="submit"]').click()
    cy.get('.alert-error').should('contain.text', 'Login and/or password are wrong')
    cy.log('✅ Validación de error de login correcta')
  })

  it('Iniciar sesión con credenciales válidas', () => {
    cy.visit('http://zero.webappsecurity.com/login.html')
    cy.get('input#user_login').type('username') // usuario válido demo
    cy.get('input#user_password').type('password') // clave válida demo
    cy.get('input[name="submit"]').click()
    cy.url().should('include', 'bank')
    cy.log('✅ Login exitoso')
  })
})
