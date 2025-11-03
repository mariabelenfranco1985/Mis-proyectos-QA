describe('Prueba de login en SauceDemo', () => {
  it('Debería mostrar error si el usuario es incorrecto', () => {
    cy.visit('https://www.saucedemo.com/')

    cy.get('[data-test="username"]').type('usuario_invalido')
    cy.get('[data-test="password"]').type('secret_sauce')
    cy.get('[data-test="login-button"]').click()

    // Validar el mensaje de error
    cy.get('[data-test="error"]').should('be.visible')
  })
})
