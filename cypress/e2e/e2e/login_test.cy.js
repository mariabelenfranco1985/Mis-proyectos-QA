describe('Prueba de Login - SauceDemo', () => {

  it('Debería iniciar sesión correctamente con credenciales válidas', () => {
    cy.visit('https://www.saucedemo.com/')

    // Escribir usuario y contraseña
    cy.get('#user-name').type('standard_user')
    cy.get('#password').type('secret_sauce')

    // Hacer clic en el botón de login
    cy.get('#login-button').click()

    // Verificar que el login fue exitoso
    cy.url().should('include', '/inventory.html')

    // Verificar que aparece el título de la página
    cy.get('.title').should('contain', 'Products')
  })

})
